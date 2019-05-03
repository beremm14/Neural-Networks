package network;

import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author emil
 */
public class WorkingNeuron extends Neuron {
    
    private final List<Connection> connections = new ArrayList<>();

    @Override
    public double getValue() {
        double sum = 0;
        for (Connection c : connections) {
            sum += c.getValue();
        }
        return sum;
    }
    
    public void addConnection(Connection c) {
        connections.add(c);
    }
    
}
