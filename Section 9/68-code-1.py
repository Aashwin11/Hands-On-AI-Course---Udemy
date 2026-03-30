#68.Static methods
class BaseUtils:
    
    @staticmethod
    def clean_ingredients(text):
       return [item.strip() for item in text.split(",")]

raw="water , milk , ginger , honey "

# obj=BaseUtils()
# obj.clean_ingredients(raw)
cleaned=BaseUtils.clean_ingredients(raw)
print(cleaned)