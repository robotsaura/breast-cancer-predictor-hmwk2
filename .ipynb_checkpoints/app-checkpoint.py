{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e24ce571",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (fsevents)\n",
      "Traceback (most recent call last):\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/ipykernel_launcher.py\", line 15, in <module>\n",
      "    from ipykernel import kernelapp as app\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/ipykernel/__init__.py\", line 5, in <module>\n",
      "    from .connect import *  # noqa\n",
      "    ^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/ipykernel/connect.py\", line 11, in <module>\n",
      "    import jupyter_client\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_client/__init__.py\", line 8, in <module>\n",
      "    from .asynchronous import AsyncKernelClient  # noqa\n",
      "    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_client/asynchronous/__init__.py\", line 1, in <module>\n",
      "    from .client import AsyncKernelClient  # noqa\n",
      "    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_client/asynchronous/client.py\", line 8, in <module>\n",
      "    from jupyter_client.client import KernelClient\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_client/client.py\", line 22, in <module>\n",
      "    from .connect import ConnectionFileMixin\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_client/connect.py\", line 27, in <module>\n",
      "    from jupyter_core.paths import jupyter_data_dir\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/jupyter_core/paths.py\", line 19, in <module>\n",
      "    from pathlib import Path\n",
      "  File \"/Users/robotsaura/anaconda3/lib/python3.11/site-packages/pathlib.py\", line 10, in <module>\n",
      "    from collections import Sequence\n",
      "ImportError: cannot import name 'Sequence' from 'collections' (/Users/robotsaura/anaconda3/lib/python3.11/collections/__init__.py)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import pickle\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the trained model\n",
    "with open(\"nb_model.pkl\", \"rb\") as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/predict\", methods=[\"POST\"])\n",
    "def predict():\n",
    "    # Retrieve user input\n",
    "    clump = float(request.form[\"clump\"])\n",
    "    cell_size = float(request.form[\"cellSize\"])\n",
    "    cell_shape = float(request.form[\"cellShape\"])\n",
    "    ad = float(request.form[\"ad\"])\n",
    "    s_cell_size = float(request.form[\"sCellSize\"])\n",
    "    nuclei = float(request.form[\"nuclei\"])\n",
    "    chromatin = float(request.form[\"chromatin\"])\n",
    "    n_nuc = float(request.form[\"nNuc\"])\n",
    "    mitosis = float(request.form[\"mitosis\"])\n",
    "    \n",
    "    # Run the input through the model for prediction\n",
    "    features = [[clump, cell_size, cell_shape, ad, s_cell_size, nuclei, chromatin, n_nuc, mitosis]]\n",
    "    prediction = model.predict(features)[0]\n",
    "    \n",
    "    # Display the prediction result\n",
    "    result = \"Benign\" if prediction == 0 else \"Malignant\"\n",
    "    \n",
    "    return f\"The predicted tumor type is: {result}\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c1fad1b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
