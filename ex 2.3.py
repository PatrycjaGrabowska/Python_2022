options = ['load data', 'export data', 'analyze & predict']

def DisplayOptions(options):
    choice = ''
    print("1 - ", options[0],"\n2 - ", options[1], "\n3 - ", options[2], "\nSelect option above or press enter to exit:")
    
    
    choice = input(choice)
    
    if choice != 0:
        
        try:
            choice_num = int(choice)
            
            if choice_num > 0 and choice_num <= len(options):
                
                if choice_num == 1:
                    choice = str(options[0])
                    print(choice)
                    
                elif choice_num == 2:
                    choice = str(options[1])
                    print(choice)
                    
                elif choice_num == 3:
                    choice = str(options[2])   
                    print(choice)
                    
            else:
                print('Error: input value should be a number from options') 
                
        except:
            print("Entered value should be a number")
            
    else:
        print("Programm termminated")

        
        
DisplayOptions(options)