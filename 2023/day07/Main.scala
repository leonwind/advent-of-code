import scala.math.Ordering.Implicits.seqOrdering

object Cards extends Enumeration {
    type Card = Value
    val Joker = Value("*")
    val Two = Value("2")
    val Three = Value("3")
    val Four = Value("4")
    val Five = Value("5")
    val Six = Value("6")
    val Seven = Value("7")
    val Eight = Value("8")
    val Nine = Value("9")
    val Ten = Value("T")
    val Jack = Value("J")
    val Queen = Value("Q")
    val King = Value("K")
    val Ace = Value("A")
}

object Day07 extends App {
    println("Solve Day 07")

    val input = io.Source.fromFile("input.txt").getLines().toList
    //println(input)

    class Hand(val cards: List[Cards.Card], val bid: Int) {

        def count: List[Int] =
            cards.groupMapReduce(card => card)(_ => 1)(_ + _).values.toList.sorted.reverse
    }

    val hands: List[Hand] = input.map {
        case s"$cards $bid" => Hand(cards.map(card => Cards.withName(card.toString)).toList, bid.toInt)
    }

    hands.map(hand => {
        //println(hand.cards)
        //println(hand.getBid)
        //println(hand.count)
    })

    val part1 = hands.sortBy(hand => (hand.count, hand.cards)).map(_.bid).zipWithIndex.map((bid, idx) => {bid * (idx + 1)}).sum
    println(part1)
}