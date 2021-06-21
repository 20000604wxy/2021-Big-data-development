import org.apache.flink.configuration.Configuration
import org.apache.flink.streaming.api.scala.{DataStream, StreamExecutionEnvironment}
import org.apache.flink.streaming.api.scala._

import java.sql.{Connection, DriverManager, PreparedStatement}

object Main {
  def main(args: Array[String]): Unit = {
    val env = StreamExecutionEnvironment.getExecutionEnvironment
    val value: DataStream[(Int, String, String, String)] = env.fromCollection(List(
      (10, "zhangsan", "12345", "张三"),
      (11, "lisi", "12345", "李四"),
      (12, "wangwu", "12345", "王五")
    ))
    value.addSink(new MySql_Sink)
    env.execute()
  }
}

import org.apache.flink.streaming.api.functions.sink.RichSinkFunction

class MySql_Sink extends RichSinkFunction[(Int, String, String, String)] {

  private var connection: Connection = null
  private var ps: PreparedStatement = null

  override def open(parameters: Configuration): Unit = {
    //1:加载驱动
    Class.forName("com.mysql.jdbc.Driver")
    //2：创建连接
    connection = DriverManager.getConnection("jdbc:mysql://bigdata130.depts.bingosoft.net:24306", "user34", "pass@bingo34")
    //3:获得执行语句
    val sql = "insert into user(id , username , password , name) values(?,?,?,?);"
    ps = connection.prepareStatement(sql)
  }

  override def invoke(value: (Int, String, String, String)): Unit = {
    try {
      //4.组装数据，执行插入操作
      ps.setInt(1, value._1)
      ps.setString(2, value._2)
      ps.setString(3, value._3)
      ps.setString(4, value._4)
      ps.executeUpdate()
    } catch {
      case e: Exception => println(e.getMessage)
    }
  }

  //关闭连接操作
  override def close(): Unit = {
    if (connection != null) {
      connection.close()
    }
    if (ps != null) {
      ps.close()
    }
  }
}
