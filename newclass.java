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
import java.applet.*;  
import java.awt.*;  
import java.awt.event.*;  
import java.util.HashSet;
import java.util.Random;
public class newclass extends Applet implements ActionListener{  
Button b1;  
TextField tf;  
 
int counter,dice,carry;
public void init()
{  
tf=new TextField();  
tf.setBounds(780,40,50,20);  
  
b1=new Button("Roll Dice");  
b1.setBounds(700,40,70,22);  
  
add(b1);add(tf);  
b1.addActionListener(this);  
 
setLayout(null);  
    
    setSize(1000,800);
    setBackground(Color.BLACK);
    
}
public void actionPerformed(ActionEvent e){  
 
  Random r = new Random();
        dice = r.nextInt(7);
        String s = Integer.toString(dice);
        tf.setText(s);
       carry=dice;
       counter=counter+carry; 
 }   
int a,b,c,d;




public void paint(Graphics g)
{
    g.setColor(Color.WHITE);
    
          a=50;
                  b=0;
                  c=50;
                  d=500;
        for(int i=0;i<=10;i++)//vertical lines
        {
                 
            a=a+50;
            c=c+50;
            g.drawLine(a,b,c,d);
        }
               a=100;
            b=50;
            c=600;
            d=50;
        for(int i=0;i<10;i++)//Horizontal lines
        {
              
            g.drawLine(a,b,c,d);
           b=b+50;
            d=d+50;
        }
   design d = new design();//Ladder Design
   d.paint(g);
    
    
}
  
  
 
}