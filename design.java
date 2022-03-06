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


public class design 
{
      
      public void paint(Graphics g)
        {
               
            
       g.setColor(Color.red);
       g.drawString("1",120,480);
      g.drawString("2",170,480);
      g.drawString("3",220,480);
      g.drawString("4",270,480);
      g.drawString("5",320,480);    //left to right
      g.drawString("6",370,480);
      g.drawString("7",420,480);
      g.drawString("8",470,480);
      g.drawString("9",520,480);
      g.drawString("10",570,480);
      
      g.setColor(Color.CYAN);
      g.drawString("11",570,430);
      g.drawString("12",520,430);
      g.drawString("13",470,430);
      g.drawString("14",420,430);
      g.drawString("15",370,430);   //right to left
      g.drawString("16",320,430);
      g.drawString("17",270,430);
      g.drawString("18",220,430);
      g.drawString("19",170,430);
      g.drawString("20",120,430);
      
      g.setColor(Color.YELLOW);
      g.drawString("21",120,380);
      g.drawString("22",170,380);
      g.drawString("23",220,380);
      g.drawString("24",270,380);
      g.drawString("25",320,380);    //left to right
      g.drawString("26",370,380);
      g.drawString("27",420,380);
      g.drawString("28",470,380);
      g.drawString("29",520,380);
      g.drawString("30",570,380);
      
      g.setColor(Color.orange);
      g.drawString("31",570,330);
      g.drawString("32",520,330);
      g.drawString("33",470,330);
      g.drawString("34",420,330);
      g.drawString("35",370,330);   //right to left
      g.drawString("36",320,330);
      g.drawString("37",270,330);
      g.drawString("38",220,330);
      g.drawString("39",170,330);
      g.drawString("40",120,330);
      
       g.setColor(Color.GREEN);
      g.drawString("41",120,280);
      g.drawString("42",170,280);
      g.drawString("43",220,280);
      g.drawString("44",270,280);
      g.drawString("45",320,280);    //left to right
      g.drawString("46",370,280);
      g.drawString("47",420,280);
      g.drawString("48",470,280);
      g.drawString("49",520,280);
      g.drawString("50",570,280);
      
      g.setColor(Color.red);
      g.drawString("51",570,230);
      g.drawString("52",520,230);
      g.drawString("53",470,230);
      g.drawString("54",420,230);
      g.drawString("55",370,230);   //right to left
      g.drawString("56",320,230);
      g.drawString("57",270,230);
      g.drawString("58",220,230);
      g.drawString("59",170,230);
      g.drawString("60",120,230);
      
      g.setColor(Color.CYAN);
      g.drawString("61",120,180);
      g.drawString("62",170,180);
      g.drawString("63",220,180);
      g.drawString("64",270,180);
      g.drawString("65",320,180);    //left to right
      g.drawString("66",370,180);
      g.drawString("67",420,180);
      g.drawString("68",470,180);
      g.drawString("69",520,180);
      g.drawString("70",570,180);
      
      g.setColor(Color.YELLOW);
      g.drawString("71",570,130);
      g.drawString("72",520,130);
      g.drawString("73",470,130);
      g.drawString("74",420,130);
      g.drawString("75",370,130);   //right to left
      g.drawString("76",320,130);
      g.drawString("77",270,130);
      g.drawString("78",220,130);
      g.drawString("79",170,130);
      g.drawString("80",120,130);
      
      g.setColor(Color.orange);
      g.drawString("81",120,80);
      g.drawString("82",170,80);
      g.drawString("83",220,80);
      g.drawString("84",270,80);
      g.drawString("85",320,80);    //left to right
      g.drawString("86",370,80);
      g.drawString("87",420,80);
      g.drawString("88",470,80);
      g.drawString("89",520,80);
      g.drawString("90",570,80);
           
      g.setColor(Color.GREEN);
      g.drawString("91",570,30);
      g.drawString("92",520,30);
      g.drawString("93",470,30);
      g.drawString("94",420,30);
      g.drawString("95",370,30);   //right to left
      g.drawString("96",320,30);
      g.drawString("97",270,30);
      g.drawString("98",220,30);
      g.drawString("99",170,30);
      g.drawString("100",112,30);    
     
      
      g.setColor(Color.WHITE);
      g.drawString("START",107,498);
      
      g.drawString("HOME",107,48);
      
      g.drawString("Snake1",405,398);
      g.drawString("Snake1",255,248);
      
       g.drawString("Snake2",455,45);
      g.drawString("Snake2",555,245);
      
       g.drawString("Snake3",405,245);
      g.drawString("Snake3",255,495);
      
       g.drawString("Snake4",255,45);
      g.drawString("Snake4",555,445);
      
      player p1= new player();
      p1.paint(g);
            
    }
}
