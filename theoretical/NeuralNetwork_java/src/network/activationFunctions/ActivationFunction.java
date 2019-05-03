package network.activationFunctions;

/**
 *
 * @author emil
 */
public interface ActivationFunction {
    
    public static Bool Bool = new Bool();
    public static HyperbolicTangent HyperbolicTangent = new HyperbolicTangent();
    public static Identity Identity = new Identity();
    public static Sigmoid Sigmoid = new Sigmoid();
    
    public double activation(double input);
    
}
