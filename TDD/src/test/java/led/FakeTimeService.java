package led;

public class FakeTimeService implements TimeServiceIntf{
    @Override
    public int getTime() {
        return 0;
    }
}
