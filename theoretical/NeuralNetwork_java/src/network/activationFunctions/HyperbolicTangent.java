package network.activationFunctions;

/**
 *
 * @author emil
 */
public class HyperbolicTangent implements ActivationFunction {

    @Override
    public double activation(double input) {
        double epx = Math.pow(Math.E, input);
        double enx = Math.pow(Math.E, -input);
        
        return (epx-enx)/(epx+enx);
    }
    
}
