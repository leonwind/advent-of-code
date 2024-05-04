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
    //val input = io.Source.fromFile("small_input.txt").getLines().toList
    val input = io.Source.fromFile("input.txt").getLines().toList

    //println(input)

    class Hand(val cards: List[Cards.Card], val bid: Int) {
        val cardsWithJoker: List[Cards.Card] = cards.map {
            case Cards.Jack => Cards.Joker
            case other => other
        }

        def count: List[Int] =
            cards.groupMapReduce(card => card)(_ => 1)(_ + _).values.toList.sorted.reverse

        def countWithJoker: List[Int] = {
            val countsWithoutJoker: List[Int] = cardsWithJoker.filter(_ != Cards.Joker).groupMapReduce(card => card)(_ => 1)(_ + _).values.toList.sorted.reverse

            if (countsWithoutJoker == Nil)
                List(5)
            else
                List(countsWithoutJoker.head + cardsWithJoker.filter(_ == Cards.Joker).length) ::: countsWithoutJoker.tail
        }
    }

    val hands: List[Hand] = input.map {
        case s"$cards $bid" => Hand(cards.map(card => Cards.withName(card.toString)).toList, bid.toInt)
    }

    hands.map(hand => {
        //println(hand.cards)
        //println(hand.getBid)
        //println(hand.countWithJoker)
    })

    val part1 = hands.sortBy(hand => (hand.count, hand.cards)).map(_.bid).zipWithIndex.map((bid, idx) => {bid * (idx + 1)}).sum
    println(part1)

    val part2 = hands.sortBy(hand => (hand.countWithJoker, hand.cardsWithJoker)).map(_.bid).zipWithIndex.map((bid, idx) => {bid * (idx + 1)}).sum
    println(part2)
}