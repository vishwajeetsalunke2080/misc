/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vishwajeet;

/**
 *
 * @author Vishwajeet Salunke
 */
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.*;
import javax.swing.*;

public class demo1 extends JFrame implements ActionListener
{
    TextField tf;
   
    demo1()
    {
       new first();
        
       tf = new TextField();
       tf.setBounds(600, 130, 170, 20);
       Button b = new Button("click me");
       b.setBounds(100, 130, 80, 30);
       b.addActionListener(this);
       add(b);
       add(tf);
        setVisible(true);
        setLayout(null);
        setBounds(50,50,200,200);
        
    }
    


    @Override
    public void actionPerformed(ActionEvent e) 
    {
        Random r = new Random();
        int a = r.nextInt(7);
        String s = Integer.toString(a);
        tf.setText(s);
        
        
        
    }
       public static void main(String args[])
       {
           
           
            new demo1();
           
       }
}
