class Magazine():
    def __init__(self,Magazine_name,adres,work_houre,income) -> None:
        self.name = Magazine_name
        self.adres = adres
        self.work_houre = work_houre
        self.income = income
    
class Book(Magazine):
    def __init__(self, name, adres, work_houre, income,Book_name, Book_autor, book_amount ,book_price,Book_grade=0) -> None:
        super().__init__(name, adres, work_houre, income)
        self.book_name = Book_name
        self.autor = Book_autor  
        self.book_amount = book_amount
        self.book_price = book_price
        self.grade = Book_grade

class CD(Magazine):
    def __init__(self, name, adres, work_houre, income,CD_type,CD_name,CD_autor,CD_amount,CD_price,CD_grade = 0) -> None:
        super().__init__(name, adres, work_houre, income)
        self.cd_type = CD_type
        self.cd_name = CD_name
        self.cd_autor = CD_autor
        self.cd_amount = CD_amount
        self.cd_price = CD_price
        self.cd_grade= CD_grade

    def functional(self,obj):
        if isinstance(obj,Customer):
            question = str(input("ნამდვილად გსურთ ნივთის შეძენა? (კი/არა): "))
            if question == "კი" and obj.budget >= self.cd_price:
                self.x = int(input("გთხოვთ შეაფასოთ წიგნი ხუთ ბალიანი სისტემით: "))
                self.cd_grade += self.x
                self.cd_amount -= 1
                obj.budget -= self.cd_price
                self.income += self.cd_price
            elif question == "არა":
                print("კარგით გმადლობთ")
            elif obj.budget <= self.cd_price:
                print("სამწუხაროთ თქვენ ბალანსზერ საკმარისი თანხა არ არის")
            else:
                question = str(input("ნამდვილად გსურთ ნივთის შეძენა? (კი/არა): "))
        else:
            print("თქვენ ვერ შეიძენთ ჩვენს პროდუქციას")
        return f"CD-ის რეიტინგი: {self.cd_grade}, CD-ის რაოდენობა: {self.cd_amount}, {obj.customer_name}-ს ბიუჯეტი: {obj.budget}, მაღაზიის შემოსავალი: {self.income}"
    
class Customer(Magazine):
    def __init__(self, Magazine_name, adres, work_houre, income, Customer_name, surname, ID, Budget) -> None:
        super().__init__(Magazine_name, adres, work_houre, income)
        self.customer_name = Customer_name
        self.surname = surname
        self.iD = ID
        self.budget = Budget 
    
a1 = Magazine("ბიბლუსი","ჭავჭავძის ქ-#160","10:00-დან 19:00-მდე",200000)
b1 = Book("ბიბლუსი","ჭავჭავძის ქ-#160","10:00-დან 19:00-მდე",200000,"მე ვხედავ მზეს", "ნოდარ დუმბაძე" , 1000 , 20 ,)
c1 = CD ("ბიბლუსი","ჭავჭავძის ქ-#160","10:00-დან 19:00-მდე",200000,"აუდიო წიგნი","მზეშინა","ლუკა კარჟალოვი",400,15,)
d1 = Customer("ბიბლუსი","ჭავჭავძის ქ-#160","10:00-დან 19:00-მდე",200000, "თომა","ხუციძე",0, 100)
print(c1.functional(d1))