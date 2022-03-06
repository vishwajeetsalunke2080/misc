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
public class player 
{
   
    int coordinates_x[]={120,170,220,270,320,370,420,470,520,570};
    int coordinates_y[]={470,470,470,470,470,470,470,470,470,470};
    
    public void paint(Graphics g)
    {
        newclass n1=new newclass();
        int carry=n1.dice;
        g.fillRect(coordinates_x[carry], coordinates_y[carry], 15, 15);
    }
}
