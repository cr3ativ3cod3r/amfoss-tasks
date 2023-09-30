from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton ,QDialog, QVBoxLayout,QHBoxLayout,QApplication
from PySide6.QtGui import QPixmap, QPalette
import os
import requests
import time


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
        enter_button.clicked.connect(self.pokemon_search)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.download_image)
        

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.disp)
        
        
        self.Name = QLabel(self)
        self.Name.setGeometry(500, 280, 160, 43)

        self.Type = QLabel(self)
        self.Type.setGeometry(500, 320, 160, 43)

        self.hp = QLabel(self)
        self.hp.setGeometry(500, 340, 160, 43)

        self.attack = QLabel(self)
        self.attack.setGeometry(500, 360, 160, 43)

        self.defense = QLabel(self)
        self.defense.setGeometry(500, 380, 160, 43)

        self.special_attack = QLabel(self)
        self.special_attack.setGeometry(500, 400, 160, 43)

        self.special_defense = QLabel(self)
        self.special_defense.setGeometry(500, 420, 160, 43)

        self.speed = QLabel(self)
        self.speed.setGeometry(500, 440, 160, 43)

        self.ability = QLabel(self)
        self.ability.setGeometry(500, 300, 360, 43)

        self.pokemon_captured = QLabel(self)
        self.pokemon_captured.setGeometry(500, 260, 360, 43)
        self.pokemon_captured.setStyleSheet("font-size: 20px; color: white; font-family: Georgia")

        self.image_label=QLabel(self)
        self.image_label.setGeometry(500,70,200,200)

        
        
        

        
	
    
    
    
    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    def pokemon_search(self):
        line_edit=self.textbox.text()
        print(line_edit)
        url=('https://pokeapi.co/api/v2/pokemon/'+line_edit)
        print(url)
        response=requests.get(url)
        data=response.json()

        if response.status_code == 200:

        
            # Add the background provided in assets
            self.BG = QPixmap('../assets/Poke_BG.jpg')
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
            
            
            self.name=data['name']
            type=data["types"][0]["type"]["name"]
            
            hp_data=data["stats"][0]["stat"]["name"]
            hp_data_stats=data["stats"][0]["base_stat"]
            

            attack_data=data["stats"][1]["stat"]["name"]
            attack_data_stats=data["stats"][1]["base_stat"]

            defense_data=data["stats"][2]["stat"]["name"]
            defense_data_stats=data["stats"][2]["base_stat"]

            specialattack_data=data["stats"][3]["stat"]["name"]
            specialattack_data_stats=data["stats"][3]["base_stat"]

            specialdefense_data=data["stats"][4]["stat"]["name"]
            specialdefense_data_stats=data["stats"][4]["base_stat"]

            speed_data=data["stats"][5]["stat"]["name"]
            speed_data_stats=data["stats"][5]["base_stat"]

            
            s=""
            for i in (data["abilities"]):
                s=s+","+str(i["ability"]["name"])
            
            # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
            self.Name.setText(f"name:{self.name}")
            self.Type.setText(f"type:{type}")
            self.hp.setText(f"{hp_data}:{hp_data_stats}")
            self.attack.setText(f"{attack_data}:{attack_data_stats}")
            self.defense.setText(f"{defense_data}:{defense_data_stats}")
            self.special_attack.setText(f"{specialattack_data}:{specialattack_data_stats}")
            self.special_defense.setText(f"{specialdefense_data}:{specialdefense_data_stats}")
            self.speed.setText(f"{speed_data}:{speed_data_stats}")
            self.ability.setText(f"ability:{s}")
            self.pokemon_captured.clear()
            
        else:
            self.name.setText("POKEMON NOT FOUND")
        
	# 2 #
    # Capture the Pokémon i.e. download the image.
    def download_image(self):
        save_folder="../store/"
        os.makedirs(save_folder,exist_ok=True)
        save_path = os.path.join(save_folder,f"{self.name}.png")
        with open(save_path,'wb') as file:
            file.write(self.data2)
        self.pokemon_captured.setText("POKEMON CAPTURED")
    	

    

    

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.

    def disp(self):

        self.image_files = [os.path.join("../store/", filename) for filename in os.listdir("../store/")]
        self.current_index=0

        

        

        window = QDialog()
        window.setWindowTitle("Poke-Display")
        window.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.image_label_2 = QLabel()
        layout.addWidget(self.image_label_2)
        
        
        
        button_layout = QHBoxLayout()
        previous_button = QPushButton("Previous")
        next_button = QPushButton("Next")

        previous_button.clicked.connect(self.previous_image)
        next_button.setStyleSheet("""
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
        
        next_button.clicked.connect(self.next_image)
        previous_button.setStyleSheet("""
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
