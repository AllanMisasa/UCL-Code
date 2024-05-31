'''
Before install for Pytorch:

Install detectron2:
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
# (add --user if you don't have permission)

# Or, to install it from a local clone:
git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2

Installing the full PyTorch setup from source will also install Detectron2 for you:
cd deepdoctection
pip install ".[source-pt]"
'''

import deepdoctection as dd
from IPython.core.display import HTML
from matplotlib import pyplot as plt

analyzer = dd.get_dd_analyzer()  # instantiate the built-in analyzer similar to the Hugging Face space demo

df = analyzer.analyze(path = "CPP/Computer Vision/2025 January/Testing/pdfs/billet.pdf")  # setting up pipeline
df.reset_state()                 # Trigger some initialization

doc = iter(df)
page = next(doc) 

image = page.viz()
plt.figure(figsize = (25,17))
plt.axis('off')
plt.imshow(image)
# Save annotated image
plt.imsave("test.png", image)
print(HTML(page.tables[0].html))
# Print OCR text
print(page.text)