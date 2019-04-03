package network;

/**
 *
 * @author emil
 */
public class InputNeuron extends Neuron {
    
    private double value;
    
    @Override
    public double getValue() {
        return value;
    }

    public void setValue(double value) {
        this.value = value;
    }

}
