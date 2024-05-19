from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model
with open("nb_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Retrieve user input
    clump = float(request.form["clump"])
    cell_size = float(request.form["cellSize"])
    cell_shape = float(request.form["cellShape"])
    ad = float(request.form["ad"])
    s_cell_size = float(request.form["sCellSize"])
    nuclei = float(request.form["nuclei"])
    chromatin = float(request.form["chromatin"])
    n_nuc = float(request.form["nNuc"])
    mitosis = float(request.form["mitosis"])
    
    # Run the input through the model for prediction
    features = [[clump, cell_size, cell_shape, ad, s_cell_size, nuclei, chromatin, n_nuc, mitosis]]
    prediction = model.predict(features)[0]
    
    # Display the prediction result
    result = "Benign" if prediction == 2 else "Malignant"
    
    return f"The predicted tumor type is: {result}"

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
