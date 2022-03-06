/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vishwajeet;

import java.awt.BorderLayout;
import javax.swing.JFrame;
import static javax.swing.JFrame.EXIT_ON_CLOSE;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.tree.DefaultMutableTreeNode;

/**
 *
 * @author Vishwajeet Salunke
 */
public class treedemo 
{
    JTree tree;
    JFrame f;
    treedemo()
            {
              f=new JFrame();
              
              f.setLayout(new BorderLayout());
                DefaultMutableTreeNode top = new DefaultMutableTreeNode("option");
                DefaultMutableTreeNode a = new DefaultMutableTreeNode("a");
                top.add(a);
                
                DefaultMutableTreeNode a1 = new DefaultMutableTreeNode("a1");
                a.add(a1);
                
                DefaultMutableTreeNode b = new DefaultMutableTreeNode("b");
                top.add(b);
                DefaultMutableTreeNode c = new DefaultMutableTreeNode("a");
                top.add(c);
                
                DefaultMutableTreeNode d = new DefaultMutableTreeNode("a1");
                a.add(d);
                
                DefaultMutableTreeNode e = new DefaultMutableTreeNode("b");
                top.add(e);
                tree = new JTree(top);
                JScrollPane jsp = new JScrollPane(tree);
                f.add(jsp,BorderLayout.CENTER);
                f.setSize(150, 150);
                f.setVisible(true);
                f.setDefaultCloseOperation(EXIT_ON_CLOSE);
            }                
             public static void main(String args[])
             {
                 treedemo t1=new treedemo();
             }
                

}
