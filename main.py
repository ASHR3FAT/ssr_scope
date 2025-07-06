
def edit_para():
    print("1. mono")
    print("2. di")
    print("3. tri")
    print("4. tetra")
    print("5. penta")
    print("6. hexa")
    print("Select which one to edit:", end=" ")
    choice = int(input())
    if(choice==1):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        mono = para_choice
    elif(choice==2):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        di = para_choice
    elif(choice==3):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        tri = para_choice
    elif(choice==4):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        tetra = para_choice
    elif(choice==5):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        penta = para_choice
    elif(choice==6):
        print("Give your new Parameter:", end=" ")
        para_choice = int(input())
        hexa = para_choice
    else:
        edit_para()

def show_para():
    print("SSR motif Length    ||     Min. number of repeats")
    print(f"mono                ||              {mono}       ")
    print(f"di                  ||              {di}         ")
    print(f"tri                 ||              {tri}        ")
    print(f"tetra               ||              {tetra}      ")
    print(f"penta               ||              {penta}      ")
    print(f"hexa                ||              {hexa}       ")

def main_page():
    print("-----Welcome to SSR Identification Tool-----")
    print("1. Check for SSR")
    print("2. View Parameters")
    print("3. Edit Parameters")
    print("4. Exit")
    print("Enter any Choice:", end=" ")
    choice = int(input())
    #if(choice==1):
    #    do_ssr()
    if(choice==2):
        show_para()
    elif(choice==3):
        edit_para()
    elif(choice==4):
        return
    else:
        print("Invalid Input")
        main_page()
    main_page()


global mono
global di
global tri
global tetra
global penta
global hexa

mono=10
di=6
tri=5
tetra=5
penta=5
hexa=5

main_page()
print("Exiting App")
