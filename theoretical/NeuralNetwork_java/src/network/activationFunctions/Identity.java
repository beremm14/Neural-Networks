package network.activationFunctions;

/**
 *
 * @author emil
 */
public class Identity implements ActivationFunction {

    @Override
    public double activation(double input) {
        return input;
    }
    
}
