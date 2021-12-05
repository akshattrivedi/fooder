import json





class Fooder:
    slots = [0,0,0,0,0,0,0]
    arrival = 0
    app = 1
    appMins = 17
    mainCourse = 2
    mainCourseMins = 29
    deliveryPerMin = 8
    maxTime = 150 # In Minutes

    def __init__(self):
        pass

    def mealsVSSlots(self, meals):
        orderSlots = self.mealsToSlotAllocation(meals)

        if orderSlots > len(self.slots):
            return False
        else:
            return True


    def allotSlots(self, distance, meals):
        len0s = 0
        orderSlots = self.mealsToSlotAllocation(meals)
        deliveryTime = None
        origSlots = list(self.slots)

        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                len0s = len0s + 1

        if len0s >= orderSlots:
            deliveryTime = self.getDeliveryTime(self.arrival, self.arrival, distance, meals)


        else:
            finalLowest = 0
            origOrderSlots = orderSlots

            while orderSlots > 0:
                lowest = self.slots[0]
                for i in range(1,len(self.slots)):
                    if self.slots[i] != 0 and self.slots[i] < lowest:
                        lowest = self.slots[i]

                for i in range(len(self.slots)):
                    updatedSlot = float('%0.1f' % (self.slots[i] - lowest))
                    if updatedSlot >= 0:
                        self.slots[i] = updatedSlot

                    if updatedSlot == 0:
                        orderSlots = orderSlots - 1

                finalLowest = finalLowest + lowest


            deliveryTime = self.getDeliveryTime(self.arrival, self.arrival + finalLowest, distance, meals)
            self.arrival = self.arrival + finalLowest
            orderSlots = origOrderSlots

        for i in range(len(self.slots)):
            if self.slots[i] == 0 and orderSlots != 0:
                self.slots[i] = float('%0.1f' % (deliveryTime))
                orderSlots = orderSlots - 1

        if deliveryTime > self.maxTime:
            self.slots = origSlots
            
        return deliveryTime

                

        
    def mealsToSlotAllocation(self, meals):
        orderSlots = 0

        for i in range(len(meals)):
            if meals[i] == "M":
                orderSlots = orderSlots + 2
            elif meals[i] == "A":
                orderSlots = orderSlots + 1

        return orderSlots
        

    def getDeliveryTime(self, prevArrival, currArrival , distance, meals):
        prepMin = 0

        if "M" in meals: # Main Course in Meals
            prepMin = self.mainCourseMins
        elif "A" in meals: # Appetizer in Meals
            prepMin = self.appMins

        return (currArrival - prevArrival) + (distance * self.deliveryPerMin) + prepMin

    def readFromInputFile(self, inputFile):
        ipFile = open(inputFile,"r")
        ipString = ""
        for line in ipFile:
            ipString = ipString + line

        return json.loads(ipString)

    def placeOrder(self, ipList):
        for i in range(len(ipList)):
            if self.mealsVSSlots(ipList[i]["meals"]):
                deliveryTime = self.allotSlots(ipList[i]["distance"], ipList[i]["meals"])
                if deliveryTime > self.maxTime:
                    #print("Order", ipList[i]["orderId"] ,": REJECTED")
                    print(f'Order {ipList[i]["orderId"]} is denied because the restaurant cannot accommodate it.')
                else:
                    #print("Order", ipList[i]["orderId"],":", deliveryTime)
                    print(f'Order {ipList[i]["orderId"]} will get delivered in {deliveryTime} minutes')

            else:
                #print("Order", ipList[i]["orderId"],": REJECTED")
                print(f'Order {ipList[i]["orderId"]} is denied because the restaurant cannot accommodate it.')



if __name__ == "__main__":
    fooder = Fooder()
    ip = fooder.readFromInputFile("input.txt")
    fooder.placeOrder(ip)