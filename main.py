import pickle
from flask import Flask, request, jsonify
from loadngo import translate

from flask_cors import CORS, cross_origin
app=Flask('app')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def splitter(sentences):
  result = []
  temp=""
  for i in range(len(sentences)):
    if sentences[i]=='?' or sentences[i]=='.' or sentences[i]=='|' or sentences[i]=='!' or sentences[i]=='।':
      if i+1<len(sentences) and (sentences[i+1]!="'" or sentences[i+1]!='"'):
        temp+=sentences[i]
        result.append(temp)
        temp=""
    else:
      temp+=sentences[i]
  result.append(temp)
  return result


@app.route('/suggest',methods=['POST'])
def predict():
    input_sentence = request.get_json()['input_sentence']
    print(input_sentence)
    sentences = splitter(input_sentence)
    print(sentences)
    results=""
    for i in range(len(sentences)):
      print(i)
      prediction = translate(sentences[i])
      print(prediction)
      results+=prediction.strip()+" "
    return jsonify({"output":results})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
