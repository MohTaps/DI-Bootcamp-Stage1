class Pagination:
    def __init__(self,items,pageSize=10):
        self.items=items
        self.pageSize=pageSize
        self.book=[]
        self.index = 0

    def getBook(self):
        for i in range(0,len(self.items),self.pageSize):
            self.book.append(self.items[i:i+self.pageSize])
    def getVisibleItems(self):
             print(self.book[self.index])
             

    def nextPage(self):
        self.index+=1
        return self
    
    def prevPage(self):
        self.index-=1
    

    def lastPage(self):
        self.index=-1
    

    def totalPages(self):
        print(f"nombre de pages: ",len(self.book))
    

    def currentPage(self):
        print(f"Page: ",self.index)
    

    def goToPage(self,page):
        if page > len(self.book):
            self.index=len(self.book)
        if page <= 0:
            self.index = 0
        self.index = page
    
    
    
if __name__=='__main__':
    alphabetList = list("abcdefghijklmnopqrstuvwqyz")
    p = Pagination(alphabetList,4)
    p.getBook()
    p.getVisibleItems()
    p.nextPage()
    p.getVisibleItems()
    p.prevPage()
    p.getVisibleItems()
    p.lastPage()
    p.getVisibleItems()
    p.totalPages()
    p.currentPage()
    p.goToPage(5)
    p.getVisibleItems()