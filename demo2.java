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
import java.applet.Applet;
import java.awt.Frame;
import java.awt.Graphics;
public class demo2 extends Applet
{
int a,b,c,d;
    public void paint (Graphics g)
    {
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