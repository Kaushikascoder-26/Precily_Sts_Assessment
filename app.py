import os
from flask import Flask, request, render_template, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer,util
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
        return jsonify({"message": "Hello"})

@app.route('/similarity', methods=['GET','POST'])
def similarity():
    if request.method == 'POST':
        print(request.get_json())
        data = request.get_json()
        text1 = data['text1']
        test_embeddings1=model.encode(text1)
        text2 = data['text2']
        test_embeddings2=model.encode(text2)
        
        # compute cosine similarity between text1 and text2
        similarity = util.cos_sim(test_embeddings1,test_embeddings2)
        
        return jsonify({"similarity_score": similarity.item() })
        # return render_template('index.html', data=similarity.item())
        # return similarity
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run()