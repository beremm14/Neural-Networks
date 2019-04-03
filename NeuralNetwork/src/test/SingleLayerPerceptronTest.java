package test;

import network.InputNeuron;
import network.NeuralNetwork;
import network.WorkingNeuron;

/**
 *
 * @author emil
 */
public class SingleLayerPerceptronTest {
    
    public static void main(String[] args) {
        NeuralNetwork nn = new NeuralNetwork();
        
        InputNeuron i1 = nn.createInput();
        InputNeuron i2 = nn.createInput();
        InputNeuron i3 = nn.createInput();
        InputNeuron i4 = nn.createInput();
        
        WorkingNeuron o1 = nn.createOutput();
        WorkingNeuron o2 = nn.createOutput();
        
        try {
            nn.fullMesh(0, 1, 2, 3, 2, 4, 5, 2);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        
        i1.setValue(2);
        i2.setValue(4);
        i3.setValue(3);
        i4.setValue(6);
        
        System.out.println(o1.getValue());
        System.out.println(o2.getValue());
    }
    
}
