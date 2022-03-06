/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vishwajeet;

import java.awt.Color;
import javax.swing.JFrame;
import javax.swing.JProgressBar;

/**
 *
 * @author Vishwajeet Salunke
 */
public class progress extends JFrame
{
    JFrame f;
    int min=0;int max=2000;
    JProgressBar bar ;
    progress()
    {
        f.setVisible(true);
        f.setSize(150, 150);
        f.setDefaultCloseOperation(f.EXIT_ON_CLOSE);
        bar = new JProgressBar(min, max);
        f.setLayout(null);
        f.add(bar);
        bar.setBorderPainted(true);
        bar.setBackground(Color.red);
        bar.setBounds(50, 50, 150, 20);
        bar.setVisible(true);
        bar.setValue(min);
                
    }
    
    public void iterate()
            {
              
                while(min<=2000)
                {
                    bar.setValue(min);
                    min=min+20;
                
                    try
                    {
                        Thread.sleep(150);
                    }
                    catch(Exception e)
                    {
                        
                    }
                }
            }
    public static void main(String args[])
    {
        progress p=new progress();
        p.iterate();
    }
}
