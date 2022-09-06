package java;


abstract class Template {
    final void templateMethod() {
        preStep();
        doWhatYouWant();
        postStep();
    }

    public abstract void doWhatYouWant();

    private void postStep() {
        System.out.println("post-step");
    }

    private void preStep() {
        System.out.println("pre-step");
    }
}

class StyleA extends Template {
    @Override
    public void doWhatYouWant() {
        System.out.println("StyleA~~");
    }
}

class StyleB extends Template {
    @Override
    public void doWhatYouWant() {
        System.out.println("StyleB");
    }
}

class Client {
    void run(Template template) {
        template.templateMethod();
    }
}

public class TemplateMethodPattern {
    public static void main(String[] args) {

        Client client = new Client();
        client.run(new StyleA());
        client.run(new StyleB());
    }
}
