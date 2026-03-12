import json
import argparse
from tqdm import tqdm
from agent import call_eval_async
from bert_score import score # bert_score is a library for computing BERT similarity score
from rouge_score import rouge_scorer # rouge score is a library for computing ROUGE score
from nltk.translate.meteor_score import meteor_score, single_meteor_score  # meteor score is a library for computing METEOR score
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


def load_result(file_path):
    results = []
    # 加载现有数据
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                results.append(json.loads(line))
        f.close()
    except FileNotFoundError:
        print(f"File {file_path} not exists.")
    except Exception as e:
        print(f"reading file error {e}")
    return results

def load_and_append(file_path, new_data):
    results = load_result(file_path)

    results.extend(new_data)
    write_results(file_path, results)

def write_results(file_path, results):
    try:
        with open(file_path, 'w') as f:
          for line in results:
            f.write(json.dumps(line)+'\n')
        print(f"new data added into {file_path}")
        f.close()
    except Exception as e:
        print(f"writing data error: {e}")

class ChatEvaluation:
  # Calculate precision, recall, F1 overall and for each domain.
  
  @staticmethod
  def get_avg(x):
    return sum([float(y) for y in x])/len(x)

  @staticmethod
  def eval(samples, type=None, question_id_to_type=None):

    if type:
      samples = [x for x in samples if question_id_to_type[x['question_id']]==type]

    predictions = [(x['question_id'], x['answer'], x['gpt4_answer'], x['result'].split('\n')[0].strip().split(' ')) for x in samples]
    result = {
      'bertscore': [],
      'meteor_score': [],
      'rouge1': [],
      'rouge2': [],
      'rougeL': [],
      'a1_score': [],
      'a2_score': [],
      'a3_score': [],
      'a4_score': [],
    }
      # bert score
    gpt4_answers = [x['gpt4_answer'] for x in samples]
    gt_answers = [x['answer'] for x in samples]
    P, R, F1 = score(gpt4_answers, gt_answers, lang='en', verbose=False)
    for i in tqdm(range(len(predictions))):
      q_id, answer, gpt4_answer, [a1_score, a2_score, a3_score, a4_score] = predictions[i]
      assert isinstance(float(a1_score), float)
      assert isinstance(float(a2_score), float)
      assert isinstance(float(a3_score), float)
      assert isinstance(float(a4_score), float)
      # rouge score
      scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
      scores = scorer.score(gpt4_answer, answer)

      rouge1 = scores['rouge1'][2]
      rouge2 = scores['rouge2'][2]
      rougeL = scores['rougeL'][2]
      
      # meteor score
      meteor_score = single_meteor_score(gpt4_answer.split(), answer.split())
      # bleu score
      bleu_score = sentence_bleu([gpt4_answer.split()], answer.split(), smoothing_function=SmoothingFunction().method1)
      
      result['bertscore'].append(F1[i])
      result['meteor_score'].append(meteor_score)
      result['rouge1'].append(rouge1)
      result['rouge2'].append(rouge2)
      result['rougeL'].append(rougeL)
      result['a1_score'].append(a1_score)
      result['a2_score'].append(a2_score)
      result['a3_score'].append(a3_score)
      result['a4_score'].append(a4_score)


    result['all'] = {
      'bertscore': ChatEvaluation.get_avg(result['bertscore']),
      'rouge1': ChatEvaluation.get_avg(result['rouge1']),
      'rouge2': ChatEvaluation.get_avg(result['rouge2']),
      'rougeL': ChatEvaluation.get_avg(result['rougeL']),
      'meteor_score': ChatEvaluation.get_avg(result['meteor_score']),
      'a1_score': ChatEvaluation.get_avg(result['a1_score']),
      'a2_score': ChatEvaluation.get_avg(result['a2_score']),
      'a3_score': ChatEvaluation.get_avg(result['a3_score']),
      'a4_score': ChatEvaluation.get_avg(result['a4_score']),
    }
    print(result['all'])

def main(args):
    ##### Load data
    reference_data = load_result(args.reference_path)
    input_data = load_result(args.input_path)
    results = load_result(args.output_path)

    if len(results) != len(input_data):
      ##### Prepare data for evaluation
      result_question_ids = set(result['question_id'] for result in results)
      sample_dict_by_id = {d['question_id']: d for d in reference_data}

      BATCH_SIZE = 15

      batch = []

      for data in input_data:
          idx = data['question_id']
          if idx in result_question_ids:
              print(f"skipping existing question_id: {idx}")
              continue
          found_dict = sample_dict_by_id.get(idx)

          if not found_dict:
              print(f"Warning: not find question_id {idx} reference, skipped...")
              continue
          data['reference_scores'] = found_dict['result']
          data['reference_answers'] = found_dict['answer']
          
          batch.append(data)

          if len(batch) >= BATCH_SIZE:
            print('processing batch...')
            async_results = call_eval_async(batch)
            results.extend(async_results)

            print(f"processed {len(results)} number of data")

            batch = []

            load_and_append(args.output_path, async_results)
      # process remaining samples
      if len(batch) > 0:
          async_results = call_eval_async(batch)
          results.extend(async_results)
          load_and_append(args.output_path, async_results)

      print(f"total number {len(results)} data")

    print('evaluating ALL')
    ChatEvaluation().eval(results)

       
    
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default=None, help='Path to the input data file (JSONL format).')
    parser.add_argument('--reference_path', type=str, default='./results_save_dir/llava-med-prediction-negative-GPT4o-eval-filtered.jsonl', help='Path to the reference data file (JSONL format).')
    parser.add_argument('--output_path', type=str, default=None, help='Path to the output results file (JSONL format).')
    args = parser.parse_args()
    main(args)



