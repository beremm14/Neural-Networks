package network.activationFunctions;

/**
 *
 * @author emil
 */
public class Sigmoid implements ActivationFunction {

    @Override
    public double activation(double input) {
        return (1. / (1. + Math.pow(Math.E, -input)));
    }
    
}
