/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package vishwajeet;

import java.applet.Applet;
import java.awt.Button;
import java.awt.FlowLayout;
import java.awt.Label;
import java.awt.Menu;
import java.awt.MenuBar;
import java.awt.MenuItem;

/**
 *
 * @author vishwajeet
 */
public class NewApplet extends Applet {

    /**
     * Initialization method that will be called after the  is loaded into
     * the browser.
     */
    public void init() 
    {
        MenuItem mi;
        setLayout(new FlowLayout());
        Label l = new Label("my label");
       Button b = new Button("my button");
       add(b);
       add(l);
      
        
    }

    // TODO overwrite start(), stop() and destroy() methods
}
