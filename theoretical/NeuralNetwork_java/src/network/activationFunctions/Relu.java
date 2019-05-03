package network.activationFunctions;

/**
 *
 * @author emil
 */
public class Relu implements ActivationFunction {

    @Override
    public double activation(double input) {
        if (input <= 0) {
            return 0;
        } else {
            return input;
        }
    }
    
}
