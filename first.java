package vishwajeet;

import java.awt.Button;
import java.awt.CheckboxGroup;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Label;
import javafx.scene.control.CheckBox;
import java.awt.*;

public class first extends Frame
{
    first()
    {

        setLayout(new FlowLayout(FlowLayout.CENTER));
        setVisible(true);
        setSize(350,350);
        Button b = new Button("my button");
        b.setVisible(true);
        Label l = new Label("hello world");
        b.setBounds(50, 50, 15, 10);
        add(l);
        add(b);
       TextField tf = new TextField("hello user",15);
        add(tf);
        TextArea ta = new TextArea("input your text here", 15, 15,15);
        add(ta);
                
        
    }
    public static void main(String args[])
    {
        new first();
    }
}

   
    

  
