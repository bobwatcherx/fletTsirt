from flet import *
from PIL import Image as ElImage
import pyscreenshot as ImageGrab
import time

def main(page:Page):
	logo = Text("logo here")

	def changetitle(e):
		# AND IF YOU  CHANGE TEXTFIELD THEN UPDATE LOGO
		logo.value = e.control.value
		page.update()

	def changesize(e):
		logo.size = e.control.value
		page.update()

	def changebold(e):
		logo.weight = "bold" if e.control.value == True else ""
		page.update()


	def changecolor(e):
		logo.color = "black" if e.control.value == "black" else "black"
		logo.color = "red" if e.control.value == "red" else "black"
		
		page.update()

	def changeloc(e:DragUpdateEvent):
		e.control.top = max(20,e.control.top + e.delta_y)
		e.control.left = max(20,e.control.left + e.delta_x)
		page.update()

	def savemyimage(e):
		# THIS WILL CHANGE AREA FOR SCREENSHOT THE TSIRT
		y = page.window_top + 10
		x = page.window_left
		# YOU CAN CHANGE 400 To you custom size
		# if you picture is cut 
		w = 400
		h = 260
		screen = ImageGrab.grab(
			bbox = (x,y,w+x,h+y)
			)
		t = str(time.time())
		# AND RENAME FILE RESULT IMAGE WITH TIME NAME
		# DEFINE IMAGE SAVE LOcATION
		myimagelocation = f"assets/{t.split('.')[0]}.png"
		screen.save(myimagelocation)
		


	# CREATE CONTAINER FOR CHANGE FONT SIZE COLOR AND BOLD
	ct_select = Container(
		bgcolor="blue200",
		padding=10,
		width=400,
		content=Column([
			Text("Select Logo",size=30),
			TextField(label="insert logo here",
				value="logo here",
				on_change=changetitle
				),
			Row([
			Text("font size : "),
			Slider(max=60,value=20,min=10,
			on_change=changesize
				),
			Checkbox(label="bold",
				value=False,
				on_change=changebold
				),
			
			
				]),
			# AND CREATE RADIO FOR CHANGE FONT COLOR
			RadioGroup(
				content=Row([
					Radio(value="black",label="black"),
					Radio(value="red",label="red"),
					
					]),
				on_change=changecolor
				),
			ElevatedButton("save My image",
				bgcolor="orange",color="white",
				on_click=savemyimage
				)
			])
		)

	# NOW I CREATE GESTURE DETECTOR FOR DRAG MY LOGO TEXT
	gd = GestureDetector(
		# YOU CURSOR IF MOUSE THEN RUN THIS FUNCTION
		mouse_cursor=MouseCursor.MOVE,
		drag_interval=10,
		content=logo,
		on_pan_update=changeloc,
		left=100,
		top=100
		)

	page.add(
		Column([
			Stack([
				Image(src="assets/baju.jpeg",
					fit="cover",
					width=300,
					height=260
					),
				gd
				]),
			ct_select
			])
		)

flet.app(target=main,assets_dir="assets")
