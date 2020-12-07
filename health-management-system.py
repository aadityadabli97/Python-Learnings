# health management system
def getdate():
    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S]")

    return current_time

def client_name():
    print("########################## WELCOME TO HEALTH MANAGEMENT SYSTEM ###############################")
    c=input("enter the client's name for whom you want to lock the file ")

    if c=="harry":
        c1 = input("there are two files of harry which file do you want to lock ")
        if c1=="harry diet":
            print("welcome to harry diet file\n")
            with open("harry diet.txt", "r+") as f1:
                f1.write("welcome to harry diet file\n")
                content1=input()
                f1.write(getdate()+"-" + content1)
                print("successfully written")

        elif c1=="harry exercise":
            print("welcome to harry exercise file\n")

            with open("harry exercise.txt", "r+") as f2:
                f2.write("welcome to harry exercise file\n")
                content2 = input()
                f2.write(getdate()+"- " + content2)
                print("successfully written")


    if c == "aaditya":
        c2 = input("there are two files of aaditya which file do you want to lock ")
        if c2 == "aaditya diet":
            print("welcome to aaditya diet file\n")

            with open("aaditya diet.txt", "w") as f3:
                content3 = input()
                f3.write("welcome to aaditya diet file\n")
                f3.write(getdate()+"-" + content3)
                print("successfully written")

        elif c2 == "aaditya exercise":
            print("welcome to aaditya exercise file ")

            with open("aaditya exercise.txt", "w") as f4:
                f4.write("welcome to aaditya's exercise file\n")
                content4 = input()
                f4.write(getdate()+" - " + content4)
                print("successfully written")


    if c == "hamad":
        c3 = input("there are two files of hamad which file do you want to lock ")
        if c3 == "hamad diet":
            print("welcome to hamad diet file\n")

            with open("hamad diet.txt", "w") as f5:
                f5.write("welcome to hamad diet file\n")
                content5=input()
                f5.write(getdate() +"- " + content5)
                print("successfully written")

        elif c3 == "hamad exercise":
            print("welcome to hamad exercise file\n")

            with open("hamad exercise.txt", "w") as f6:
                f6.write("welcome to hamad exercise file\n")
                content6 = input()
                f6.write(getdate() + "- "+ content6)
                print("successfully written")


if __name__ == '__main__':

    client_name()