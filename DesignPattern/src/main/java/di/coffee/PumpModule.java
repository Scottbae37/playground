package di.coffee;

import dagger.Binds;
import dagger.Module;

@Module
abstract class PumpModule {
  /**
   * interface나 추상 클래스에 @Provides 대신 사용,
   *
   * 하나의 Parameter 만 받는 추상 메소드를 정의해야하고 리턴타입은 반드시 그 하나의 Parameter 의
   * 상위 인터페이스(또는 추상클래스)가 되어야 합니다
   *
   */
  @Binds
  abstract Pump providePump(Thermosiphon pump);
}
