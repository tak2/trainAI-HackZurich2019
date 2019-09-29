package com.example.hackzurich.ui.dashboard

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.hackzurich.R
import kotlinx.android.synthetic.main.item_tickets.view.*
import androidx.lifecycle.MutableLiveData


/**
 * Created by Amr on 9/28/2019.
 */
class TicketsAdapter : RecyclerView.Adapter<TicketsAdapter.TicketViewHolder>() {

    private var ticketsList = emptyList<Ticket>()

    val clickListener=MutableLiveData<Ticket>()


    fun notifyTickets(tickets: List<Ticket>) {
        ticketsList = tickets
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): TicketViewHolder {
val view=LayoutInflater.from(parent.context).inflate(R.layout.item_tickets,parent,false)
    return TicketViewHolder(view,listener = clickListener)
    }

    override fun getItemCount(): Int {
        return ticketsList.size
    }

    override fun onBindViewHolder(holder: TicketViewHolder, position: Int) {
        holder.onBind(ticketsList[holder.adapterPosition])
    }


    class TicketViewHolder(private val view: View,val listener:MutableLiveData<Ticket>) : RecyclerView.ViewHolder(view) {
         fun onBind(ticket: Ticket)
         {
             view.tvTicketName.text=ticket.ticketName
             view.tvTechnicianName.text="Mina Rezkalla"
             view.tvTicketState.text=TicketState.OPEN.state
             view.setOnClickListener {
                 listener.value=ticket
             }
         }
    }
}

 enum class TicketState(val state:String)
{
    CLOSED("Closed"),
    INPROGRESS("In Progress"),
    OPEN("Open")
}