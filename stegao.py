from stegano import lsb
# hide a message in an image
def hide():
    image_path = input("Enter the path of image to hide messages on: ")
    message = input("Enter the message to hide: ")
    lsb.hide(image_path, message).save("image_with_message.png")


# reveal the hidden message
def reveal():
    image_path = input("Enter the path of the image to reveal the message: ")
    hidden_message = lsb.reveal(image_path)
    print("Hidden message:", hidden_message)


choice = input("Press 'H' to hide message or Press 'R' to reveal message: ")
if(choice.lower() == 'h'):
     hide()   
elif(choice.lower() == 'r'):
    reveal()
else:
    print("wrong input!")