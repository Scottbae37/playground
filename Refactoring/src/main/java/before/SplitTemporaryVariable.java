package before;

public class SplitTemporaryVariable {
  static class Distance {
    int _delay = 1;
    double _primaryForce = 1, _secondaryForce = 1;
    double _mass = 1;

    double getDistanceTravelled(int time) {
      double result;
      double acc = _primaryForce / _mass;
      int primaryTime = Math.min(time, _delay);
      result = 0.5 * acc * primaryTime * primaryTime;

      int secondaryTime = time - _delay;
      if (secondaryTime > 0) {
        double primaryVel = acc * _delay;
        acc = (_primaryForce + _secondaryForce) / _mass;
        result += primaryVel * secondaryTime + 0.5 * acc * secondaryTime * secondaryTime;
      }

      return result;
    }
  }
}
