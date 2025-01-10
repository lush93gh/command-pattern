from invoker.j_button import JButton
from command.angel_listener import AngelListener
from command.devil_listener import DevilListener

class SwingObserverExample:
     
    #  The Client is the class that sets up the 
    #  Swing components and sets the commands 
    #  (AngelListener and DevilListener) in the 
    #  Invoker (the Button).
     
     def __init__(self):
          # Set up ...

          # The button is our Invoker. The button 
          # calls the actionPerformed() (like 
          # execute()) methods in the commands (the 
          # ActionListeners) when you click the button.
          button = JButton("Should I do it?")

          # AngelListener and DevilListener 
          # are our concrete Commands. They 
          # implement the command interface (in 
          # this case, ActionListener).
          button.add_action_listener(AngelListener())
          button.add_action_listener(DevilListener())
