# kivySamples
Kivy 1.10.11 Samples


## Setting up Kivy

python -m pip install --upgrade pip setuptools wheel virtualenv
python -m virtualenv kivy_venv

If you're in windows cmd shell do:

kivy_venv\Scripts\activate

otherwise do:

source kivy_venv/Scripts/activate


Next do (note that to install the new kivy rc2 you need to add --pre to pip):

pip install kivy_deps.glew kivy_deps.sdl2 kivy_deps.gstreamer kivy kivy_examples --pre
python kivy_venv/share/kivy-examples/demo/kivycatalog/main.py
