package com.example.hackzurich.ui.dashboard

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProviders
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.hackzurich.R
import kotlinx.android.synthetic.main.fragment_dashboard.*


class DashboardFragment : Fragment() {

    private lateinit var dashboardViewModel: DashboardViewModel
    private val adapter=TicketsAdapter()


    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        dashboardViewModel =
            ViewModelProviders.of(this).get(DashboardViewModel::class.java)
        val root = inflater.inflate(R.layout.fragment_dashboard, container, false)
        dashboardViewModel.getTickets().observe(this, Observer {
            it?.let {
                adapter.notifyTickets(it)
            }

        })
        return root
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        initTicketsRecyclerView()
    }

    private fun initTicketsRecyclerView() {
        val manager=LinearLayoutManager(context)
        rclTickets.setHasFixedSize(true)
        rclTickets.layoutManager=manager
        rclTickets.adapter=adapter
        adapter.clickListener.observe(this, Observer {
            val gmmIntentUri = Uri.parse("google.navigation:q=${it.latitude},${it.longitude}")
            val mapIntent = Intent(Intent.ACTION_VIEW, gmmIntentUri)
            mapIntent.setPackage("com.google.android.apps.maps")
            startActivity(mapIntent)
        })
    }
}