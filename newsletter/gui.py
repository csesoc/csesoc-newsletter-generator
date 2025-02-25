import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QLineEdit, QTextEdit, QPushButton, QScrollArea, 
                            QGroupBox, QFormLayout, QMessageBox, QFrame)
from PyQt5.QtCore import Qt
from scrapers.facebook import Event
from scrapers.media import Article
from scrapers.opportunities import Opportunity

class NewsletterGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSESoc Newsletter Generator")
        self.setMinimumSize(800, 600)
        
        # Store data
        self.events = []
        self.articles = []
        self.opportunities = []
        
        # Main container
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # Main layout
        main_layout = QVBoxLayout(main_widget)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)
        
        # Create content widget for the scroll area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        scroll_area.setWidget(content_widget)
        
        # Create header
        self.create_header(content_layout)
        
        # Create sections
        self.create_events_section(content_layout)
        self.create_articles_section(content_layout)
        self.create_opportunities_section(content_layout)
        
        # Create generate button
        self.create_generate_button(content_layout)
        
        # Add stretch to push everything to the top
        content_layout.addStretch()
        
    def create_header(self, layout):
        header_label = QLabel("CSESoc Newsletter Generator")
        header_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        header_label.setAlignment(Qt.AlignCenter)
        
        description_label = QLabel("Add events, articles, and opportunities for the newsletter")
        description_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(header_label)
        layout.addWidget(description_label)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)
        
    def create_events_section(self, layout):
        self.events_group = QGroupBox("Events")
        events_layout = QVBoxLayout(self.events_group)
        
        # Container for event forms
        self.events_container = QVBoxLayout()
        events_layout.addLayout(self.events_container)
        
        # Add button
        add_event_btn = QPushButton("Add Event")
        add_event_btn.clicked.connect(self.add_event_form)
        events_layout.addWidget(add_event_btn)
        
        layout.addWidget(self.events_group)
    
    def create_articles_section(self, layout):
        self.articles_group = QGroupBox("Media Articles")
        articles_layout = QVBoxLayout(self.articles_group)
        
        # Container for article forms
        self.articles_container = QVBoxLayout()
        articles_layout.addLayout(self.articles_container)
        
        # Add button
        add_article_btn = QPushButton("Add Article")
        add_article_btn.clicked.connect(self.add_article_form)
        articles_layout.addWidget(add_article_btn)
        
        layout.addWidget(self.articles_group)
    
    def create_opportunities_section(self, layout):
        self.opportunities_group = QGroupBox("Opportunities")
        opportunities_layout = QVBoxLayout(self.opportunities_group)
        
        # Container for opportunity forms
        self.opportunities_container = QVBoxLayout()
        opportunities_layout.addLayout(self.opportunities_container)
        
        # Add button
        add_opportunity_btn = QPushButton("Add Opportunity")
        add_opportunity_btn.clicked.connect(self.add_opportunity_form)
        opportunities_layout.addWidget(add_opportunity_btn)
        
        layout.addWidget(self.opportunities_group)
    
    def create_generate_button(self, layout):
        generate_btn = QPushButton("Generate Newsletter")
        generate_btn.setStyleSheet("font-size: 16px; padding: 10px;")
        generate_btn.clicked.connect(self.generate_newsletter)
        layout.addWidget(generate_btn)
    
    def add_event_form(self):
        # Create a group box for the event form
        event_form = QGroupBox()
        event_form.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 5px; margin-top: 10px; }")
        form_layout = QFormLayout(event_form)
        
        # Form fields
        url_input = QLineEdit()
        title_input = QLineEdit()
        time_input = QLineEdit()
        location_input = QLineEdit()
        img_input = QLineEdit()
        desc_input = QTextEdit()
        desc_input.setMaximumHeight(100)
        
        form_layout.addRow("Event URL:", url_input)
        form_layout.addRow("Event Title:", title_input)
        form_layout.addRow("Event Time:", time_input)
        form_layout.addRow("Event Location:", location_input)
        form_layout.addRow("Image URL:", img_input)
        form_layout.addRow("Description:", desc_input)
        
        # Create buttons
        buttons_layout = QHBoxLayout()
        
        event_ref = {"form": event_form}  # Reference to form for the closure
        
        def save_event():
            event = Event(
                url=url_input.text(),
                title=title_input.text(),
                description=desc_input.toPlainText(),
                time=time_input.text(),
                location=location_input.text(),
                img=img_input.text()
            )
            self.events.append(event)
            # Show confirmation
            QMessageBox.information(self, "Success", "Event saved successfully!")
        
        def delete_form():
            self.events_container.removeWidget(event_ref["form"])
            event_ref["form"].deleteLater()
        
        save_button = QPushButton("Save Event")
        save_button.clicked.connect(save_event)
        
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(delete_form)
        
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(delete_button)
        
        form_layout.addRow(buttons_layout)
        
        # Add to container
        self.events_container.addWidget(event_form)
    
    def add_article_form(self):
        # Create a group box for the article form
        article_form = QGroupBox()
        article_form.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 5px; margin-top: 10px; }")
        form_layout = QFormLayout(article_form)
        
        # Form fields
        url_input = QLineEdit()
        title_input = QLineEdit()
        img_input = QLineEdit()
        desc_input = QTextEdit()
        desc_input.setMaximumHeight(100)
        
        form_layout.addRow("Article URL:", url_input)
        form_layout.addRow("Article Title:", title_input)
        form_layout.addRow("Image URL:", img_input)
        form_layout.addRow("Description:", desc_input)
        
        # Create buttons
        buttons_layout = QHBoxLayout()
        
        article_ref = {"form": article_form}  # Reference to form for the closure
        
        def save_article():
            article = Article(
                url=url_input.text(),
                title=title_input.text(),
                description=desc_input.toPlainText(),
                img=img_input.text()
            )
            self.articles.append(article)
            # Show confirmation
            QMessageBox.information(self, "Success", "Article saved successfully!")
        
        def delete_form():
            self.articles_container.removeWidget(article_ref["form"])
            article_ref["form"].deleteLater()
        
        save_button = QPushButton("Save Article")
        save_button.clicked.connect(save_article)
        
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(delete_form)
        
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(delete_button)
        
        form_layout.addRow(buttons_layout)
        
        # Add to container
        self.articles_container.addWidget(article_form)
    
    def add_opportunity_form(self):
        # Create a group box for the opportunity form
        opportunity_form = QGroupBox()
        opportunity_form.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 5px; margin-top: 10px; }")
        form_layout = QFormLayout(opportunity_form)
        
        # Form fields
        title_input = QLineEdit()
        desc_input = QTextEdit()
        desc_input.setMaximumHeight(100)
        
        form_layout.addRow("Opportunity Title:", title_input)
        form_layout.addRow("Description:", desc_input)
        
        # Create buttons
        buttons_layout = QHBoxLayout()
        
        opportunity_ref = {"form": opportunity_form}  # Reference to form for the closure
        
        def save_opportunity():
            opportunity = Opportunity(
                title=title_input.text(),
                description=desc_input.toPlainText()
            )
            self.opportunities.append(opportunity)
            # Show confirmation
            QMessageBox.information(self, "Success", "Opportunity saved successfully!")
        
        def delete_form():
            self.opportunities_container.removeWidget(opportunity_ref["form"])
            opportunity_ref["form"].deleteLater()
        
        save_button = QPushButton("Save Opportunity")
        save_button.clicked.connect(save_opportunity)
        
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(delete_form)
        
        buttons_layout.addWidget(save_button)
        buttons_layout.addWidget(delete_button)
        
        form_layout.addRow(buttons_layout)
        
        # Add to container
        self.opportunities_container.addWidget(opportunity_form)
    
    def generate_newsletter(self):
        try:
            from main import generate_newsletter
            result = generate_newsletter(self.events, self.articles, self.opportunities)
            QMessageBox.information(self, "Success", f"Newsletter generated successfully! File saved as {result}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating newsletter: {str(e)}")

def launch_gui():
    app = QApplication(sys.argv)
    window = NewsletterGeneratorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()