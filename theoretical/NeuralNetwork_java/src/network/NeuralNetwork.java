package network;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author emil
 */
public class NeuralNetwork {
    
    private final List<InputNeuron> inputNeurons = new ArrayList<>();
    private final List<WorkingNeuron> outputNeurons = new ArrayList<>();
    
    
    
    
    public InputNeuron createInput() {
        InputNeuron in = new InputNeuron();
        inputNeurons.add(in);
        return in;
    }
    
    public WorkingNeuron createOutput() {
        WorkingNeuron on = new WorkingNeuron();
        outputNeurons.add(on);
        return on;
    }
    
    public void fullMesh() {
        for (WorkingNeuron on : outputNeurons) {
            for (InputNeuron in  : inputNeurons) {
                on.addConnection(new Connection(in, 0));
            }
        }
    }
    
    public void fullMesh(double... weights) throws Exception {
        if(weights.length != inputNeurons.size() * outputNeurons.size()) {
            throw new Exception("Wrong weights...");
        }
        
        int index = 0;
        for (WorkingNeuron on : outputNeurons) {
            for (InputNeuron in  : inputNeurons) {
                on.addConnection(new Connection(in, weights[index++]));
            }
        }
    }
    
}
