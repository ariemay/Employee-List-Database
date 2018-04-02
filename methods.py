class Method:

    def inputData(name, position, base):
        name.append(input("Name: "))
        position.append(input("Position: "))
        base.append(input("Base: "))

    # def widthName(self, name):
    #     nameWidth = len(name[idx])
    #     if nameWidth > 9:
    #         return 9 - nameWidth
    #     else:
    #         return 9
    #
    # def widthPosition(self, position):
    #     positionWidth = len(position[idx])
    #     if positionWidth > 9:
    #         return 9 - positionWidth
    #     else:
    #         return 9
    #
    # def widhtBase(self, base):
    #     baseWidth = len(base[idx])
    #     if baseWidth > 9:
    #         return 9 - baseWidth
    #     else:
    #         return 9

    def showData(name, position, base):
        print("| No | Employee ", " " * 10, "| Position", " " * 10, " | Base ", " " * 10, "|")
        no = 0
        for i in name:
            idx = name.index(i)
            no = no + 1
            print("|", no, " |",
                  name[idx], " " * 10, "|",
                  position[idx], " " * 10, "|",
                  base[idx], " " * 10, "|")

    def continueQuestion(name, position, base):
        answer = input("Want to start over? ")
        if answer == "yes":
            Method.inputData(name, position, base)
            Method.continueQuestion(name, position, base)
        elif answer == "no":
            Method.showData(name, position, base)
