package network;

/**
 *
 * @author emil
 */
public class Connection {
    private final Neuron neuron;
    private double weight;

    public Connection(Neuron neuron, double weight) {
        this.neuron = neuron;
        this.weight = weight;
    }
    
    public double getValue() {
        return neuron.getValue() * weight;
    }
}
