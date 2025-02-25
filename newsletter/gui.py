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
        
        # Store forms instead of data
        self.event_forms = []
        self.article_forms = []
        self.opportunity_forms = []
        
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
        
        # Store form inputs reference for later collection
        form_data = {
            "url": url_input,
            "title": title_input,
            "time": time_input,
            "location": location_input,
            "img": img_input,
            "desc": desc_input,
            "form": event_form
        }
        self.event_forms.append(form_data)
        
        # Delete button only
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_event_form(form_data))
        form_layout.addRow(delete_button)
        
        # Add to container
        self.events_container.addWidget(event_form)
    
    def add_article_form(self):
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
        
        # Store form inputs reference for later collection 
        form_data = {
            "url": url_input,
            "title": title_input,
            "img": img_input,
            "desc": desc_input,
            "form": article_form
        }
        self.article_forms.append(form_data)
        
        # Delete button only
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_article_form(form_data))
        form_layout.addRow(delete_button)
        
        # Add to container
        self.articles_container.addWidget(article_form)
    
    def add_opportunity_form(self):
        opportunity_form = QGroupBox()
        opportunity_form.setStyleSheet("QGroupBox { border: 1px solid gray; border-radius: 5px; margin-top: 10px; }")
        form_layout = QFormLayout(opportunity_form)
        
        # Form fields
        title_input = QLineEdit()
        desc_input = QTextEdit()
        desc_input.setMaximumHeight(100)
        
        form_layout.addRow("Opportunity Title:", title_input)
        form_layout.addRow("Description:", desc_input)
        
        # Store form inputs reference for later collection
        form_data = {
            "title": title_input,
            "desc": desc_input,
            "form": opportunity_form
        }
        self.opportunity_forms.append(form_data)
        
        # Delete button only
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_opportunity_form(form_data))
        form_layout.addRow(delete_button)
        
        # Add to container
        self.opportunities_container.addWidget(opportunity_form)
    
    def generate_newsletter(self):
        try:
            # Collect all data from forms
            events = []
            for form in self.event_forms:
                event = Event(
                    url=form["url"].text(),
                    title=form["title"].text(),
                    description=form["desc"].toPlainText(),
                    time=form["time"].text(),
                    location=form["location"].text(),
                    img=form["img"].text()
                )
                events.append(event)
                
            articles = []
            for form in self.article_forms:
                article = Article(
                    url=form["url"].text(),
                    title=form["title"].text(),
                    description=form["desc"].toPlainText(),
                    img=form["img"].text()
                )
                articles.append(article)
                
            opportunities = []
            for form in self.opportunity_forms:
                opportunity = Opportunity(
                    title=form["title"].text(),
                    description=form["desc"].toPlainText()
                )
                opportunities.append(opportunity)

            # Generate newsletter with collected data
            from main import generate_newsletter
            result = generate_newsletter(events, articles, opportunities)
            QMessageBox.information(self, "Success", f"Newsletter generated successfully! File saved as {result}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating newsletter: {str(e)}")
    
    def delete_event_form(self, form_data):
        self.events_container.removeWidget(form_data["form"])
        form_data["form"].deleteLater()
        self.event_forms.remove(form_data)

    def delete_article_form(self, form_data):
        self.articles_container.removeWidget(form_data["form"])
        form_data["form"].deleteLater()
        self.article_forms.remove(form_data)

    def delete_opportunity_form(self, form_data):
        self.opportunities_container.removeWidget(form_data["form"])
        form_data["form"].deleteLater()
        self.opportunity_forms.remove(form_data)

def launch_gui():
    app = QApplication(sys.argv)
    window = NewsletterGeneratorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()