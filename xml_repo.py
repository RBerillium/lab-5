import xml.etree.ElementTree as ET
import os
from models import *



class UserXMLRepository:
    def __init__(self, xml_file: str):
        self.xml_file = xml_file
        
        # Проверяем, существует ли файл
        if not os.path.exists(xml_file):
            # Создаём пустой XML-документ с корневым элементом
            root = ET.Element("Users")
            tree = ET.ElementTree(root)
            tree.write(xml_file)
        
        # Загружаем существующий или только что созданный XML
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def add(self, user: User):
        # Создаём новый XML-элемент для пользователя
        user_elem = ET.Element("User")
        ET.SubElement(user_elem, "UserID").text = str(user.user_id)
        ET.SubElement(user_elem, "Name").text = user.name
        ET.SubElement(user_elem, "Age").text = str(user.age)
        ET.SubElement(user_elem, "Gender").text = user.gender
        ET.SubElement(user_elem, "Weight").text = str(user.weight)
        ET.SubElement(user_elem, "Height").text = str(user.height)

        # Добавляем элемент в XML
        self.root.append(user_elem)
        self.tree.write(self.xml_file)

    def get_all(self) -> List[User]:
        # Используем XPath для извлечения всех пользователей
        users = []
        for user_elem in self.root.findall("User"):
            user = User(
                user_id=int(user_elem.find("UserID").text),
                name=user_elem.find("Name").text,
                age=int(user_elem.find("Age").text),
                gender=user_elem.find("Gender").text,
                weight=float(user_elem.find("Weight").text),
                height=float(user_elem.find("Height").text),
            )
            users.append(user)
        return users

    def find_by_id(self, user_id: int) -> User:
        # Используем XPath для поиска пользователя по ID
        user_elem = self.root.find(f"User[UserID='{user_id}']")
        if user_elem is None:
            return None
        return User(
            user_id=int(user_elem.find("UserID").text),
            name=user_elem.find("Name").text,
            age=int(user_elem.find("Age").text),
            gender=user_elem.find("Gender").text,
            weight=float(user_elem.find("Weight").text),
            height=float(user_elem.find("Height").text),
        )
