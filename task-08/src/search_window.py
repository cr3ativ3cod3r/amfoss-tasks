from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton ,QDialog, QVBoxLayout,QHBoxLayout,QApplication
from PySide6.QtGui import QPixmap, QPalette
import os
import requests


class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
       
        self.w = None        
        self.setFixedSize(850, 500)
        self.textbox = QLineEdit(self)
        
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: dark-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                font-family: Georgia;
                text-align: center;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)
      

        
        self.BG = QPixmap('../assets/landing.jpg')
        self.BG_Palette=QPalette()
        self.BG_Palette.setBrush(QPalette.Window,self.BG)
        self.setPalette(self.BG_Palette)
        setScaledContents=True

        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.abc)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.download_image)
        

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.disp)
        
        
        self.label2 = QLabel(self)
        self.label2.setGeometry(500, 280, 160, 43)

        self.label3 = QLabel(self)
        self.label3.setGeometry(500, 320, 160, 43)

        self.label4 = QLabel(self)
        self.label4.setGeometry(500, 340, 160, 43)

        self.label5 = QLabel(self)
        self.label5.setGeometry(500, 360, 160, 43)

        self.label6 = QLabel(self)
        self.label6.setGeometry(500, 380, 160, 43)

        self.label7 = QLabel(self)
        self.label7.setGeometry(500, 400, 160, 43)

        self.label8 = QLabel(self)
        self.label8.setGeometry(500, 420, 160, 43)

        self.label9 = QLabel(self)
        self.label9.setGeometry(500, 440, 160, 43)

        self.label10 = QLabel(self)
        self.label10.setGeometry(500, 300, 360, 43)

        self.label11 = QLabel(self)
        self.label11.setGeometry(500, 260, 360, 43)
        self.label11.setStyleSheet("font-size: 20px; color: white; font-family: Georgia")

        self.image_label=QLabel(self)
        self.image_label.setGeometry(500,70,200,200)

        
        
        

        
	
    
    
    
    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    def abc(self):
        line_edit=self.textbox.text()
        print(line_edit)
        url=('https://pokeapi.co/api/v2/pokemon/'+line_edit)
        print(url)
        response=requests.get(url)
        data=response.json()

        if response.status_code == 200:

        

            self.BG = QPixmap('../assets/Poke_bG.jpg')
            self.BG_Palette.setBrush(QPalette.Window,self.BG)
            self.setPalette(self.BG_Palette)
            
            official_artwork=data['sprites']['other']['official-artwork']['front_default']
            response2=requests.get(official_artwork)
            self.data2=response2.content

            self.image = QPixmap()
            self.image_label.clear()
            self.image.loadFromData(self.data2)
            self.image_label.setPixmap(self.image)
            self.image_label.setScaledContents(True)
            #self.image_label.show()
            
            self.name=data['name']
            type=data["types"][0]["type"]["name"]
            
            ability=data["stats"][0]["stat"]["name"]
            ability_b=data["stats"][0]["base_stat"]
            

            ability2=data["stats"][1]["stat"]["name"]
            ability_2b=data["stats"][1]["base_stat"]

            ability3=data["stats"][2]["stat"]["name"]
            ability_3b=data["stats"][2]["base_stat"]

            ability4=data["stats"][3]["stat"]["name"]
            ability_4b=data["stats"][3]["base_stat"]

            ability5=data["stats"][4]["stat"]["name"]
            ability_5b=data["stats"][4]["base_stat"]

            ability6=data["stats"][5]["stat"]["name"]
            ability_6b=data["stats"][5]["base_stat"]

            
            s=""
            for i in (data["abilities"]):
                s=s+","+str(i["ability"]["name"])
            
            
            self.label2.setText(f"name:{self.name}")
            self.label3.setText(f"type:{type}")
            self.label4.setText(f"{ability}:{ability_b}")
            self.label5.setText(f"{ability2}:{ability_2b}")
            self.label6.setText(f"{ability3}:{ability_3b}")
            self.label7.setText(f"{ability4}:{ability_4b}")
            self.label8.setText(f"{ability5}:{ability_5b}")
            self.label9.setText(f"{ability6}:{ability_6b}")
            self.label10.setText(f"ability:{s}")
            # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
        else:
            self.label2.setText("POKEMON NOT FOUND")
        
	
    def download_image(self):
        save_folder="../store/"
        os.makedirs(save_folder,exist_ok=True)
        save_path = os.path.join(save_folder,f"{self.name}.png")
        #print(save_path)
        with open(save_path,'wb') as file:
            file.write(self.data2)
        self.label11.setText("POKEMON CAPTURED")
    	

    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

    def disp(self):

        self.image_files = [os.path.join("../store/", filename) for filename in os.listdir("../store/")]
        self.current_index=0

        #app = QApplication([])

        

        window = QDialog()
        window.setWindowTitle("Image Viewer")
        window.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.image_label_2 = QLabel()
        layout.addWidget(self.image_label_2)
        
        button_layout = QHBoxLayout()
        previous_button = QPushButton("Previous")
        next_button = QPushButton("Next")

        previous_button.clicked.connect(self.previous_image)
        next_button.clicked.connect(self.next_image)

        button_layout.addWidget(previous_button)
        button_layout.addWidget(next_button)

        layout.addLayout(button_layout)

        window.setLayout(layout)

        self.show_image()

        window.exec()

    def show_image(self):
        if 0 <= self.current_index < len(self.image_files):
            image_path = self.image_files[self.current_index]
            pixmap = QPixmap(image_path)
            self.image_label_2.setPixmap(pixmap)
            
            
            #image_label.setAlignment(Qt.AlignCenter)
        else:
            image_path = self.image_files[0]
            self.current_index=0
            pixmap = QPixmap(image_path)
            self.image_label_2.setPixmap(pixmap)

    def next_image(self):
        self.current_index
        self.current_index += 1
        self.show_image()

    def previous_image(self):
        self.current_index
        self.current_index -= 1
        self.show_image()
        


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())