/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vishwajeet;

import java.awt.Frame;
import java.util.Set;
import javax.swing.JScrollPane;
import javax.swing.JTable;

/**
 *
 * @author Vishwajeet Salunke
 */
public class jTree extends Frame
{
    public static void main(String args[])
    {
        Frame f = new Frame("myFrame");
        
        
        String rows [][] ={{"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"},{"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"},{"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"},
                            {"101","gj","5456","sdfsdf"}};
        String col[]={"gdfg","fgdfg","gdfg","gdfg"};
        JTable jt = new JTable(rows,col);
        jt.setToolTipText("Hello nigga");
        JScrollPane jsp = new JScrollPane(jt);
        
        
        f.add(jsp);
        f.setSize(50,500);
        f.setVisible(true);
    }
}
