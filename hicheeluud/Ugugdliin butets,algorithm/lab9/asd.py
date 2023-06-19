class Node:  #node gdg class uusgey
    def __init__(self, data):  #node gdg class maani baiguulagch funkts baiguulay. baiguulagch funkts maani neg argument awna. ter ni data 
        #buyu  ugugdul awax ystoi 
        self.left = None #left bhin bol zuuntaldaa
        self.right = None 
        self.data = data #self iin datad ni dataginh n utgig onoogood ugchixnu

    def insert(self, data): #6.baiguulax funkts maani insert uildel xiidg funkts bnga. insert uildel maani mun adil data gdg neg argument awna
        if self.data: 
            #7.xerwee selfiin data n xooson bh ym bol xoosnoos ylgaatai uyd yu xiix we gdgiig zaaj ugnu. ene data maani ugugdulq bna gdg maani mod yruusu binary search dr maani ymr c ugugdulq bnaa gsn ug
            #10. if self.data: end xerwee utgagui bh ym bol else ruu usreed ene uilddig xiine
            if data < self.data: 
                #11.ene utgatai bla gj bodoy.utgatai bhin bol utgin baga uu ugui yu gdgiin shalgana.baga nhin bol zuun ix bhyn bol baruun 
                # gd tawichixna
                ##12. herwee gadnaas orj irex data gdg argumentin utga ni selfin datagaas ers baga bol zuun muchirnuudlu shiljij orno
                if self.left is None: #13.daxiad nuxtsul shalgay xerwee selfiin left gdg zuil ni xooson bh toxioldold yhwee gdgig shalgaj uzne 
                    #herw zuun muchir maani xooson bwl ene bol uuruu zuun muchrrin xamgiin parent node bolno
                    self.left = Node(data) #14.selfinxee leftd utga onoox ni node classin funktsee duudaad ugugdulduu blhr datag oruulna
                else: #15. esreg toxioldold xerwee ugugdultei bwl yh we gwl
                    self.left.insert(data) #16.selfiin left muchirnuud dund insert uildlee axiad duudchixna gsn ug. thr zuun muchir zuun 
                    #talruga bugd dawtagdaad ywaad bna
            elif data > self.data: #17.xerwee elif toxioldold data maani selfiin datagaas ix toxioldold yhwe gwl baruun muchir lu orno gsn ug
                if self.right is None: #18.selfiin right iig shalgaj uzne.right maanu exleed xooson bnu gdgig 
                    self.right = Node(data) #19.xerwee xooson bh ym bol right-tdaa ene bol shine node uusj bna gegdiig onoogd ugchixnu
                else: #20.xerwee xooson bish bh ym bol
                    self.right.insert(data) #21.baruun muchirnuud dund insert uildliig axiad dawtaad xj ugnu za ingd insert uildel maani yrunxidu blj bna
        else: #8.xerwee else toxioldold ymr uildel xiix we gwl syni node claasinxaa obyectig zrlaad utga onoogd ugchixnu 
            self.data = data #9.selfinxee datad utga onoox ni datagaa onoogd ugchixuy. 

    def printTree(self): #22.daraagin baiguulagch funkst maani blhr binary treege xewlex funkst bna enige printTree gd nerley
        if self.left: #23.ene funkst maani bux zuun bolon baruun muchruudig bugdin xewlene gsn ug.exleed zuun muchruu shalgay 
            #baga utguud n bga uchraas
            self.left.printTree() #24.left bhin bol selfiin left iig odo ene  bichij bga funktsee duudaad ugchixnu texeer bux zuun muchruud 
            #xewlegden gsn ug
        print(self.data) #25.ene nuxtsul biylsen biyleeq xamaaq axiad selfiinxaa datag zalgax ni 
        if self.right: #26.xerwee self right gj bh ym bol bs rightin bugdiin xwlene gsn ug
            self.right.printTree() #27.printTree funktsee duudaad ugchixnu

bst = Node(50) #28.
bst.insert(40) #29. insert funktse duudna
bst.insert(60)
bst.insert(41)
bst.insert(35)
# bst.insert(3)
# bst.insert(93)
# bst.insert(123)

bst.printTree()